import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { DbService } from '../../services/db.service';
import { Router } from '@angular/router'

@Component({
  selector: 'app-new-poll',
  templateUrl: './new-poll.component.html',
  styleUrls: ['./new-poll.component.css']
})
export class NewPollComponent implements OnInit {

	poll_data_payload: FormGroup;

  constructor(
  	private fbuilder: FormBuilder,
  	private db_service: DbService,
  	private router: Router,
  ) { }

  ngOnInit() {
  	this.poll_data_payload = this.fbuilder.group({
			"question": this.fbuilder.control("", Validators.required),
			"question_type": this.fbuilder.control("single"),
			"options": this.fbuilder.control([]),
			"answer_limit": this.fbuilder.control(3),
			"participant_count": this.fbuilder.control(0),
			"timer": this.fbuilder.control(300, Validators.required),
			"show_result_on": this.fbuilder.control(""),
			"is_anonymous": this.fbuilder.control(true),
			"owner": this.fbuilder.control(2)
		});
  }

  validate() {
  	if(this.poll_data_payload.status == 'VALID'){
  		this.new_poll();
  	}
  }

  new_poll() {
  	const payload = this.poll_data_payload.value;
  	this.db_service.new_poll(payload).subscribe(res => {
  		if(res.success) {
  			// alert("new poll created");
  			this.router.navigate(['./attempt/'+res.data.id]);
  		}
  	});
  }

}
