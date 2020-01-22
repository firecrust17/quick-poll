import { Component, OnInit } from '@angular/core';
import { DbService } from '../../services/db.service';

@Component({
  selector: 'app-poll-history',
  templateUrl: './poll-history.component.html',
  styleUrls: ['./poll-history.component.css']
})
export class PollHistoryComponent implements OnInit {

	user_id;
	created_polls = [];
	other_polls = [];

  constructor(
  	private db_service: DbService,
  ) { }

  ngOnInit() {
  	this.user_id = parseInt(localStorage.getItem('poll_user'))
  	this.get_user_polls();
  }

  get_user_polls() {
  	const payload = {"owner": this.user_id};
  	this.db_service.get_user_polls(payload).subscribe(res => {
  		if(res.success) {
  			this.created_polls = res.data.created_polls;
  			this.other_polls = res.data.other_polls;
  		}
  	});
  }

}
