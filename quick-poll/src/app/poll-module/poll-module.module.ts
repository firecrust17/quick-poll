import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { PollModuleRoutingModule } from './poll-module-routing.module';
import { NewPollComponent } from './new-poll/new-poll.component';
import { PollHistoryComponent } from './poll-history/poll-history.component';
import { PollResultsComponent } from './poll-results/poll-results.component';
import { AttemptPollComponent } from './attempt-poll/attempt-poll.component';

@NgModule({
  declarations: [
    NewPollComponent,
    PollHistoryComponent,
    PollResultsComponent,
    AttemptPollComponent
  ],
  imports: [
    CommonModule,
    PollModuleRoutingModule
  ]
})
export class PollModuleModule { }
