import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { NewPollComponent } from './new-poll/new-poll.component';
import { PollHistoryComponent } from './poll-history/poll-history.component';
import { PollResultsComponent } from './poll-results/poll-results.component';
import { AttemptPollComponent } from './attempt-poll/attempt-poll.component';
import { PollLoginComponent } from './poll-login/poll-login.component';

const routes: Routes = [
	{
		path: 'new',
		component: NewPollComponent
	},
	{
		path: 'history/:user_id',
		component: PollHistoryComponent
	},
	{
		path: 'results/:poll_id',
		component: PollResultsComponent
	},
	{
		path: 'attempt/:poll_id',
		component: AttemptPollComponent
	},
	{
		path: 'login',
		component: PollLoginComponent
	},
	{
		path: 'login/:poll_id',
		component: PollLoginComponent
	},
	{
		path: '**',
		redirectTo: '/new'
	},
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class PollModuleRoutingModule { }
