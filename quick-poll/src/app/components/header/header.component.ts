import { Component, OnInit } from '@angular/core';
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

  constructor() { }

  ngOnInit() {
  }

}
