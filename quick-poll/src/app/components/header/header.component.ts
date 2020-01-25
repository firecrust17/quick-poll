import { Component, OnInit } from '@angular/core';
import { Router, NavigationStart, Event } from '@angular/router';
import { faSignOutAlt, faChartPie, faUser } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {

	faIcons = {
		"logout": faSignOutAlt,
		"logo": faChartPie,
		"user": faUser,
	};
	poll_user_name = null;

  constructor(
  	private router: Router
  ) {
		this.router.events.subscribe( (event: Event) => {
			if (event instanceof NavigationStart) {
				if(localStorage.getItem('poll_user_name') != null) {
					this.poll_user_name = localStorage.getItem('poll_user_name');
				} else {
					this.poll_user_name = null;
				}
			}
		});

	}

  ngOnInit() {
  }

  logout() {
  	localStorage.removeItem("poll_user");
  	localStorage.removeItem("poll_user_name");
  	this.router.navigate(['./login']);
  }

}
