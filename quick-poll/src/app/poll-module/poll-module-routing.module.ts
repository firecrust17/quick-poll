import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { NewPollComponent } from './new-poll/new-poll.component';
import { PollHistoryComponent } from './poll-history/poll-history.component';
import { PollResultsComponent } from './poll-results/poll-results.component';
import { AttemptPollComponent } from './attempt-poll/attempt-poll.component';

const routes: Routes = [
	{
		path: 'new',
		component: NewPollComponent
	},
	{
		path: 'history',
		component: PollHistoryComponent
	},
	{
		path: 'results',
		component: PollResultsComponent
	},
	{
		path: 'attempt/:id',
		component: AttemptPollComponent
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
