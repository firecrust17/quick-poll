import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class EnvService {
  
  public service_host = 'http://localhost';
  public service_port = 8000;
  public service_url  = this.service_host+':'+this.service_port;

  constructor() { }
}
