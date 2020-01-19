import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { DbService } from '../../services/db.service';

@Component({
  selector: 'app-poll-results',
  templateUrl: './poll-results.component.html',
  styleUrls: ['./poll-results.component.css']
})
export class PollResultsComponent implements OnInit {

	poll_id;
	results: any = {};

  constructor(
  	private _activatedRoute: ActivatedRoute,
    private db_service: DbService,
  ) {
  	this._activatedRoute.params.subscribe(params => {
      this.poll_id = params.poll_id;
    });
  }

  ngOnInit() {
  	this.get_poll_results();
  }

  get_poll_results() {
  	const payload = {"poll_hash": this.poll_id};
  	this.db_service.get_poll_results(payload).subscribe(res => {
  		if(res.success && res.count) {
  			// console.log(res.data);
  			this.results = res.data;
  		}
  	});
  }

}
