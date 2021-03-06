import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import {Md5} from "md5-typescript";
import { ToastrService } from 'ngx-toastr';

import { DbService } from '../../services/db.service';

import { faSignInAlt, faUserPlus } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-poll-login',
  templateUrl: './poll-login.component.html',
  styleUrls: ['./poll-login.component.css']
})
export class PollLoginComponent implements OnInit {

  faIcons = {
    "login": faSignInAlt,
    "signup": faUserPlus
  };

	is_new = true;
	poll_id = null;
	login_payload: FormGroup;
	signup_payload: FormGroup;

  constructor(
  	private fbuilder: FormBuilder,
  	private _activatedRoute: ActivatedRoute,
  	private router: Router,
    private db_service: DbService,
    private toastr: ToastrService,
  ) {
  	this._activatedRoute.params.subscribe(params => {
      if(params.poll_id != undefined){
      	this.poll_id = params.poll_id;
      }
    });
  }

  ngOnInit() {
  	this.login_payload = this.fbuilder.group({
			"email": this.fbuilder.control("", [Validators.required/*, Validators.email*/]),
			"password": this.fbuilder.control("", Validators.required),
		});

  	this.signup_payload = this.fbuilder.group({
			"user_name": this.fbuilder.control("", Validators.required),
			"email": this.fbuilder.control("", [Validators.required/*, Validators.email*/]),
			"password": this.fbuilder.control("", Validators.required),
			"confirm_password": this.fbuilder.control("", Validators.required),
		});

  }

  login_user() {
  	var payload = this.login_payload.value;
    payload['email'] = payload['email'].toLowerCase();
    payload['password'] = Md5.init(Md5.init(payload['password']));
  	this.db_service.login_user(payload).subscribe(res => {
  		if(res.success){
  			this.redirect_user(res);
  		}
  	});
  }

  create_user() {
  	var payload = this.signup_payload.value;
    payload['email'] = payload['email'].toLowerCase();
    payload['password'] = Md5.init(Md5.init(payload['password']));
  	this.db_service.create_user(payload).subscribe(res => {
  		if(res.success){
  			this.redirect_user(res);
  		}
  	});
  }

  redirect_user(res) {
    localStorage.setItem('poll_user', res.data.id);
    localStorage.setItem('poll_user_name', res.data.user_name);
  	if(this.poll_id){
  		this.router.navigate(['./attempt/'+this.poll_id]);
  	} else {
  		this.router.navigate(['./new']);
  	}
  }

  check_valid_email(email) {
    var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    return regex.test(email);
  }

  validate(type) {
  	if(type == 'login'){
  		if(this.login_payload.status == 'VALID'){
  			if(this.check_valid_email(this.login_payload.get('email').value)) {
          this.login_user();
        } else {
          this.toastr.error('', 'Invalid Email');
        }
  		} else {
  			this.toastr.error('', 'All fields are mandatory');
  		}
  	} else if (type == 'signup') {
  		if(this.signup_payload.status == 'VALID'){
  			if(this.signup_payload.get('password').value == this.signup_payload.get('confirm_password').value){
  				if(this.check_valid_email(this.signup_payload.get('email').value)) {
            this.create_user();
          } else {
            this.toastr.error('', 'Invalid Email');
          }
  			} else {
          this.toastr.error('', 'Passwords did not match');
  			}
  		} else {
        this.toastr.error('', 'All fields are mandatory');
  		}
  	}
  }

}
