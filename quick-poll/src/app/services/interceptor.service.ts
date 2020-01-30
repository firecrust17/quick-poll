import { Injectable } from '@angular/core';
import { HttpEvent, HttpInterceptor, HttpHandler, HttpRequest, HttpResponse, HttpErrorResponse } from '@angular/common/http';
// import { EnvService } from './env.service';
import { ToastrService } from 'ngx-toastr';
import { Observable, of } from 'rxjs';
import { tap, catchError } from "rxjs/operators";

import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class InterceptorService implements HttpInterceptor {

  constructor(
  	// private env: EnvService,
  	private toastr: ToastrService,
  	private router: Router,
  ) { }


  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {

		if (req.method == 'POST'){

			return next.handle(req).pipe(
				tap((event: HttpEvent<any>) => {
					if (event instanceof HttpResponse && event.body.success != undefined && !event.body.success) {
						this.toastr.error('', event.body.message);
						// if(event.body.error_code == 121){
						// 	// do nothing on specific error code
						// }
					}
				}),
			);

		} else {
			return next.handle(req);
		}
	}


}
