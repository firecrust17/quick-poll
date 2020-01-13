import { Component, OnInit, OnDestroy } from '@angular/core';
// import { Socket } from 'ngx-socket-io';
import { SocketService } from '../../services/socket.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-attempt-poll',
  templateUrl: './attempt-poll.component.html',
  styleUrls: ['./attempt-poll.component.css']
})
export class AttemptPollComponent implements OnInit, OnDestroy {

	// active_users = 0;
	attempt_count = 0;
	total_members = 0;
	time_left = 5; 	//	seconds
	time_elapsed = false;
	interval;

	has_attempted = false;

  id;

  constructor(
    private socket: SocketService,
    private _activatedRoute: ActivatedRoute
  ) {
    this._activatedRoute.params.subscribe(params => {
      this.id = params.id;
      this.socket.initiate_connection({"room": params.id, "user_id": 123, "user_name": "Aneesh"});
      this.socket.socket_event('join-room', this.id);
    });
  }

  ngOnInit() {

    this.socket.get_data_all().subscribe(res => {
      console.log(res.data);
      this.process_response(res);
    });

    // setTimeout(() => {
      // this.socket.join_room(this.id);
    // }, 1000);

  	this.interval = setInterval(() => {
  		if(--this.time_left == 0){
  			this.time_out()
        // this.socket.room_users();
  		}
  	}, 1000);
  	// this.socket.io.emit('join_room', {"room": "id"});

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
  	this.has_attempted = true;		
  	// this.socket.emit('broad-cast', {id: "id"});
  }

  attempt() {
  	console.log("save result");
  	this.has_attempted = true;
    this.socket.socket_event('data_in_all', this.id, {type: "attempted"});
  }

  show_result() {
  	console.log("show result");
  	this.has_attempted = true;
  }

  ngOnDestroy() {
    this.socket.io.emit('disconnect', {'event_type': 'disconnect', 'room': this.id});
  }

}
