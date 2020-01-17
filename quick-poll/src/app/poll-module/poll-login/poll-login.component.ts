import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { DbService } from '../../services/db.service';

@Component({
  selector: 'app-poll-login',
  templateUrl: './poll-login.component.html',
  styleUrls: ['./poll-login.component.css']
})
export class PollLoginComponent implements OnInit {

	is_new = true;
	poll_id = null;
	login_payload: FormGroup;
	signup_payload: FormGroup;

  constructor(
  	private fbuilder: FormBuilder,
  	private _activatedRoute: ActivatedRoute,
  	private router: Router,
    private db_service: DbService,
  ) {
  	this._activatedRoute.params.subscribe(params => {
      if(params.poll_id != undefined){
      	this.poll_id = params.poll_id;
      }
    });
  }

  ngOnInit() {
  	this.login_payload = this.fbuilder.group({
			"email": this.fbuilder.control("", Validators.required),
			"password": this.fbuilder.control("", Validators.required),
		});

  	this.signup_payload = this.fbuilder.group({
			"user_name": this.fbuilder.control("", Validators.required),
			"email": this.fbuilder.control("", Validators.required),
			"password": this.fbuilder.control("", Validators.required),
			"confirm_password": this.fbuilder.control("", Validators.required),
		});

  }

  login_user() {
  	const payload = this.login_payload.value;
  	this.db_service.login_user(payload).subscribe(res => {
  		if(res.success){
  			localStorage.setItem('poll_user', res.data.id);
  			this.redirect_user();
  		}
  	});
  }

  create_user() {
  	const payload = this.signup_payload.value;
  	this.db_service.create_user(payload).subscribe(res => {
  		if(res.success){
  			localStorage.setItem('poll_user', res.data.id);
  			this.redirect_user();
  		}
  	});
  }

  redirect_user() {
  	if(this.poll_id){
  		this.router.navigate(['./attempt/'+this.poll_id]);
  	} else {
  		this.router.navigate(['./new']);
  	}
  }

  validate(type) {
  	if(type == 'login'){
  		if(this.login_payload.status == 'VALID'){
  			this.login_user();
  		} else {
  			alert("All fields are mandatory");
  		}
  	} else if (type == 'signup') {
  		if(this.signup_payload.status == 'VALID'){
  			if(this.signup_payload.get('password').value == this.signup_payload.get('confirm_password').value){
  				this.create_user();
  			} else {
  				alert("Passwords did not match");
  			}
  		} else {
  			alert("All fields are mandatory");
  		}
  	}
  }

}
