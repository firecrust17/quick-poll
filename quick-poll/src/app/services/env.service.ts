import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class EnvService {

  public service_host = 'http://localhost';
  public service_port = 8000;
  public service_url  = this.service_host+':'+this.service_port;
  public domain  = this.service_host+':4200';

  public io_host = 'localhost';
  public io_port = '3001';
  public io_namespace = 'test';
  public io_url = 'http://'+this.io_host+':'+this.io_port+'/'+this.io_namespace;

  constructor() { }
}
