import { Component, OnInit } from '@angular/core';
import { DbService } from '../../services/db.service';
import { EnvService } from '../../services/env.service';
import { ToastrService } from 'ngx-toastr';

import { faPoll, faCopy } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-poll-history',
  templateUrl: './poll-history.component.html',
  styleUrls: ['./poll-history.component.css']
})
export class PollHistoryComponent implements OnInit {

	faIcons = {
    "chart": faPoll,
    "copy": faCopy,
  };

	user_id;
	created_polls = [];
	other_polls = [];

  constructor(
  	private db_service: DbService,
  	private toastr: ToastrService,
  	private env: EnvService,
  ) { }

  ngOnInit() {
  	this.user_id = parseInt(localStorage.getItem('poll_user'))
  	this.get_user_polls();
  }

  get_user_polls() {
  	const payload = {"owner": this.user_id};
  	this.db_service.get_user_polls(payload).subscribe(res => {
  		if(res.success) {
  			this.created_polls = res.data.created_polls;
  			this.other_polls = res.data.other_polls;
  		}
  	});
  }

  copy_link(index) {
  	var copyText = $("#poll_link_"+index);
    copyText.select();
    // copyText.setSelectionRange(0, 99999); /*For mobile devices*/
    document.execCommand("copy");
    this.toastr.success('', 'Link Copied');
  }

}
