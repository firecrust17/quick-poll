import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { EnvService } from './env.service';

@Injectable({
  providedIn: 'root'
})
export class DbService {

  constructor(
  	private http: HttpClient,
  	private env: EnvService,
  ) { }

  private new_poll_url = `${this.env.service_url}/new_poll`;
  new_poll(payload) {
  	return this.http.post<any>(this.new_poll_url, payload);
  }

  private get_poll_data_url = `${this.env.service_url}/get_poll_data`;
  get_poll_data(payload) {
  	return this.http.post<any>(this.get_poll_data_url, payload);
  }

  private get_attempt_count_url = `${this.env.service_url}/get_attempt_count`;
  get_attempt_count(payload) {
  	return this.http.post<any>(this.get_attempt_count_url, payload);
  }

  private has_attempted_url = `${this.env.service_url}/has_attempted`;
  has_attempted(payload) {
  	return this.http.post<any>(this.has_attempted_url, payload);
  }

  private login_user_url = `${this.env.service_url}/login_user`;
  login_user(payload) {
  	return this.http.post<any>(this.login_user_url, payload);
  }

  private create_user_url = `${this.env.service_url}/create_user`;
  create_user(payload) {
  	return this.http.post<any>(this.create_user_url, payload);
  }

  private get_user_polls_url = `${this.env.service_url}/get_user_polls`;
  get_user_polls(payload) {
  	return this.http.post<any>(this.get_user_polls_url, payload);
  }

  private answer_poll_url = `${this.env.service_url}/answer_poll`;
  answer_poll(payload) {
  	return this.http.post<any>(this.answer_poll_url, payload);
  }

  private get_poll_results_url = `${this.env.service_url}/get_poll_results`;
  get_poll_results(payload) {
  	return this.http.post<any>(this.get_poll_results_url, payload);
  }


}
