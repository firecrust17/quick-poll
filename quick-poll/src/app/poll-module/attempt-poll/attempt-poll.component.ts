import { Component, OnInit, OnDestroy } from '@angular/core';
// import { Socket } from 'ngx-socket-io';
import { SocketService } from '../../services/socket.service';
import { ActivatedRoute, Router } from '@angular/router';
import { DbService } from '../../services/db.service';
import { EnvService } from '../../services/env.service';
import { ToastrService } from 'ngx-toastr';

import * as $ from 'jquery';

import { faStopwatch, faCheck, faPoll, faCopy } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-attempt-poll',
  templateUrl: './attempt-poll.component.html',
  styleUrls: ['./attempt-poll.component.css']
})
export class AttemptPollComponent implements OnInit, OnDestroy {

  faIcons = {
    "submit": faCheck,
    "timer": faStopwatch,
    "chart": faPoll,
    "copy": faCopy,
  };

	// active_users = 0;
  user_id;
  poll_data:any = {};
	attempt_count = 0;
	total_members = 0;
	time_left = 0; 	//	seconds
	time_elapsed = false;
	interval;
  poll_link = '';

  option_array = [];
  option_input = "";

	attempted = false;

  id;

  constructor(
    private socket: SocketService,
    private _activatedRoute: ActivatedRoute,
    private router: Router,
    private db_service: DbService,
    private env: EnvService,
    private toastr: ToastrService,
  ) {
    this._activatedRoute.params.subscribe(params => {
      this.id = params.poll_id;
      this.poll_link = this.env.domain+"/attempt/"+params.poll_id;
      if(localStorage.getItem('poll_user')){
        this.user_id = parseInt(localStorage.getItem('poll_user'))
      } else {
        this.router.navigate(['./login/'+this.id]);
      }
      this.socket.initiate_connection({"room": this.id, "user_id": this.user_id, "user_name": "Aneesh"});
      this.socket.socket_event('join_room', this.id);
    });
  }

  ngOnInit() {


    this.socket.get_data_all().subscribe(res => {
      console.log(res);
      this.process_response(res);
    });

    this.get_poll_data();
    this.get_attempt_count();
    this.has_attempted();

    // setTimeout(() => {
      // this.socket.join_room(this.id);
    // }, 1000);

  	
  	// this.socket.io.emit('join_room', {"room": "id"});

  }

  get_poll_data(){
    const payload = {"id": this.id};
    this.db_service.get_poll_data(payload).subscribe(res => {
      if(res.success){

        this.poll_data = res.data;
        for(var i=0; i<this.poll_data.options.length; i++) {
          this.option_array[i] = false;
        }
        this.total_members = res.data.participant_count;
        // console.log(this.poll_data);

        this.calculate_and_start_timer();

      }
    });
  }

  get_attempt_count() {
    const payload = {"poll_hash": this.id};
    this.db_service.get_attempt_count(payload).subscribe(res => {
      if(res.success) {
        this.attempt_count = res.data;
      }
    });
  }

  has_attempted() {
    const payload = {"poll_hash": this.id, "user_id": this.user_id};
    this.db_service.has_attempted(payload).subscribe(res => {
      if(res.success) {
        this.attempted = res.data;
      }
    });
  }

  calculate_and_start_timer() {
    // this.poll_data
    // this.time_left
    const now: any = new Date();
    const time: any = new Date(this.poll_data.created_on);

    this.time_left = this.poll_data.timer - Math.round((now-time)/1000)

    if(this.time_left > 0){
      this.interval = setInterval(() => {
        if(--this.time_left <= 0){
          this.time_out()
          // this.socket.room_users();
        }
      }, 1000);
    } else {
      this.time_left = 0;
      this.time_out()
    }
  }

  clear_if_single(event, index) {
    // console.log(event.target.checked)
    if(this.poll_data.question_type == 'single') {
      if(event.target.checked){
        for(var i=0; i<this.option_array.length; i++) {
          if(i != index){
            this.option_array[i] = false;
            $('#opt'+i).prop('checked', false);
          }
        }
        this.option_array[index] = true;
      } else {
        for(var i=0; i<this.option_array.length; i++) {
          this.option_array[i] = false;
          $('#opt'+i).prop('checked', false);
        }
      }

    } else if(this.poll_data.question_type == 'multiple') {
      this.option_array[index] = event.target.checked;
      $('#opt'+index).prop('checked', event.target.checked);

    } else {
      // do nothing
    }
  }

  process_response(res) {
    switch(res.event_type) {
      case 'join_room':
        // set total count if variable empty
        // increment total count if variable already set        
        console.log(res.count + " users connected to this room");
      break;
      case 'disconnect':
        console.log(res.data);
      break;
      case 'data_in_all':
        // switch

        this.process_data_out_all(res.data);

      break;
      default:
      break;
    }
  }

  process_data_out_all(data) {
    switch(data.type) {
      case 'attempted':
        // increment attempt count
        this.attempt_count++;
        // this.get_attempt_count();
      break;

    }
  }

  send() {
    this.socket.socket_event('data_in_all', this.id, {type: "attempted"});
  }

  time_out() {
  	// console.log("clear");
  	clearInterval(this.interval);
  	this.time_elapsed = true;
  	this.attempted = true;		
  	// this.socket.emit('broad-cast', {id: "id"});
  }

  answer_poll() {
    const payload = this.prepare_payload();
    if(!payload.answer.length) {
      this.toastr.error('', 'Please select an answer to submit');
      return false;
    }
    this.db_service.answer_poll(payload).subscribe(res => {
      if(res.success) {
      	this.attempted = true;
        this.socket.socket_event('data_in_all', this.id, {type: "attempted"});
      } else if (res.error_code == 1) {
        this.attempted = true;
      }
    });
  }

  prepare_payload() {
    var answer = [];
    if(this.poll_data.question_type == 'input') {
      answer[0] = this.option_input;
    } else {
      for(var i=0; i<this.option_array.length; i++) {
        if(this.option_array[i]){
          answer.push(this.poll_data.options[i]['option']);
        }
      }
    }
    // console.log(answer);

    return {"answer": answer, "answered_by": this.user_id, "id_poll_data": this.poll_data.id};
  }

  show_result() {
  	this.router.navigate(['./results/'+this.id]);
    // this.router.navigate(['./login']);
  }

  copy_link() {

    var copyText = $("#poll_link");
    copyText.select();
    // copyText.setSelectionRange(0, 99999); /*For mobile devices*/
    document.execCommand("copy");
    
    // var $temp = $("#poll_link");
    // $("body").append($temp);
    // $temp.val($(element).html()).select();
    // document.execCommand("copy");
    // $temp.remove();
    
    // alert("Copied the text: " + copyText.value);
    this.toastr.success('', 'Link Copied');

  }

  ngOnDestroy() {
    this.socket.io.close();
  }

}
