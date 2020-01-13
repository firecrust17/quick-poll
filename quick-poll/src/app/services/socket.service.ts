import { Injectable } from '@angular/core';
import * as io from 'socket.io-client';
import { Observable } from 'rxjs/Observable';

@Injectable({
  providedIn: 'root'
})
export class SocketService {

	public namespace = 'test';
	public url = 'http://localhost:3001/'+this.namespace;
	public io: any;

  constructor() {}

  initiate_connection(params) {
  	this.io = io(this.url, {autoConnect: false, query: params});
  	this.io.connect();
  }

  // join_room(event_type, room) {
  // 	this.io.emit(event_type, {"event_type": event_type, "room": room});
  // }

  // send_data_all(event_type, room) {
  // 	this.io.emit(event_type, {"event_type": event_type, "room": room});
  // }

  socket_event(event_type, room, data=null) {
  	this.io.emit(event_type, {"event_type": event_type, "room": room, "data": data});
  }

  get_data_all() {
  	return Observable.create((observer) => {
      this.io.on('data_out_all', (data) => {
        observer.next(data);
      });
    });
  }

}
