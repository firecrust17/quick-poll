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


}
