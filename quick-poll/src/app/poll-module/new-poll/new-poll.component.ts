import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators, FormArray } from '@angular/forms';
import { DbService } from '../../services/db.service';
import { Router } from '@angular/router'
import { ToastrService } from 'ngx-toastr';

import * as $ from 'jquery';

import { faInfoCircle, faPlayCircle, faTimes, faPlus } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-new-poll',
  templateUrl: './new-poll.component.html',
  styleUrls: ['./new-poll.component.css']
})
export class NewPollComponent implements OnInit {

  faIcons = {
    "info": faInfoCircle,
    "start": faPlayCircle,
    "delete": faTimes,
    "add": faPlus,
  };

	poll_data_payload: FormGroup;
  poll_user;
  choice = ["Amsterdam", "London", "Bangkok", "Switzerland", "Peru", "New York", "Mauritius", "Goa", "Singapore", "Running out of places..", "But you arent!", "Carry on :)", "Good luck!", "..."]

  constructor(
  	private fbuilder: FormBuilder,
  	private db_service: DbService,
  	private router: Router,
    private toastr: ToastrService,
  ) { }

  ngOnInit() {
    if(!localStorage.getItem('poll_user')){
      this.router.navigate(['./login']);
    } else {
      this.poll_user = parseInt(localStorage.getItem('poll_user'));
    }

  	this.poll_data_payload = this.fbuilder.group({
			"question": this.fbuilder.control("", Validators.required),
			"question_type": this.fbuilder.control("single"),
			"options": this.fbuilder.array([]),
			"answer_limit": this.fbuilder.control(3),
			"participant_count": this.fbuilder.control(0),
			"timer": this.fbuilder.control(5, Validators.required),
			"show_result_on": this.fbuilder.control(""),
			"is_anonymous": this.fbuilder.control(true),
			"id_user": this.fbuilder.control(this.poll_user)
		});
    this.add_option();
    setTimeout(() => {
      $('#question').focus();
    },300);
  }
  get formArray() { return <FormArray>this.poll_data_payload.get('options'); }

  validate() {
  	if(this.poll_data_payload.status == 'VALID' && this.formArray.status == 'VALID'){
  		this.new_poll();
  	} else {
      this.toastr.error('', 'Please enter all mandatory fields');
    }
  }

  new_poll() {
  	var payload = this.poll_data_payload.value;
    payload['timer'] *= 60;
  	this.db_service.new_poll(payload).subscribe(res => {
  		if(res.success) {
  			// alert("new poll created");
  			this.router.navigate(['./attempt/'+res.data.poll_hash]);
  		}
  	});
  }

  add_option(type=null) {
    if(type == 'one') {
      if(this.formArray['controls']['length'] >= 1) {
        return;
      }
    }
    const control = <FormArray>this.poll_data_payload.controls['options'];
    control.push(
      this.fbuilder.group({
        // 'id': this._fb.control(-1),
        'option': this.fbuilder.control('', Validators.required),
      })
    );
    setTimeout(() => {
      $('#option_'+(control.length-1)).focus();
    }, 200);
    return false;
  }

  remove_option(index) {
    this.formArray.removeAt(index);
    return false;
  }

  clear_options() {
    // this.formArray.clear();
    this.poll_data_payload.controls['options'] = this.fbuilder.array([]);
  }

  update_qtype(type) {
    this.poll_data_payload.patchValue({"question_type": type});
  }

}
