import { Component, OnInit, OnDestroy } from '@angular/core';
// import { Socket } from 'ngx-socket-io';
import { SocketService } from '../../services/socket.service';
import { ActivatedRoute } from '@angular/router';
import { DbService } from '../../services/db.service';

@Component({
  selector: 'app-attempt-poll',
  templateUrl: './attempt-poll.component.html',
  styleUrls: ['./attempt-poll.component.css']
})
export class AttemptPollComponent implements OnInit, OnDestroy {

	// active_users = 0;
  user_id;
  poll_data:any = {};
	attempt_count = 0;
	total_members = 0;
	time_left = 0; 	//	seconds
	time_elapsed = false;
	interval;

	attempted = false;

  id;

  constructor(
    private socket: SocketService,
    private _activatedRoute: ActivatedRoute,
    private db_service: DbService,
  ) {
    this._activatedRoute.params.subscribe(params => {
      this.id = parseInt(params.id);
      this.user_id = parseInt(localStorage.getItem('poll_user'))
      this.socket.initiate_connection({"room": params.id, "user_id": this.user_id, "user_name": "Aneesh"});
      this.socket.socket_event('join-room', params.id);
    });
  }

  ngOnInit() {


    this.socket.get_data_all().subscribe(res => {
      console.log(res.data);
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
        this.total_members = res.data.participant_count;
        // console.log(this.poll_data);

        this.calculate_and_start_timer();

      }
    });
  }

  get_attempt_count() {
    const payload = {"id_poll_data": this.id};
    this.db_service.get_attempt_count(payload).subscribe(res => {
      if(res.success) {
        this.attempt_count = res.data;
      }
    });
  }

  has_attempted() {
    const payload = {"poll_id": this.id, "user_id": this.user_id};
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
      break;

    }
  }

  send() {
    this.socket.socket_event('data_in_all', this.id, this.id);
  }

  time_out() {
  	// console.log("clear");
  	clearInterval(this.interval);
  	this.time_elapsed = true;
  	this.attempted = true;		
  	// this.socket.emit('broad-cast', {id: "id"});
  }

  attempt() {
  	console.log("save result");
  	this.attempted = true;
    this.socket.socket_event('data_in_all', this.id, {type: "attempted"});
  }

  show_result() {
  	console.log("show result");
  	this.attempted = true;
  }

  ngOnDestroy() {
    this.socket.io.emit('disconnect', {'event_type': 'disconnect', 'room': this.id});
  }

}
