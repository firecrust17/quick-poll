import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
// const config: SocketIoConfig = { url: 'http://localhost:3001/test', options: {} };

// import { SocketIoModule, SocketIoConfig } from 'ngx-socket-io';

import { PollModuleRoutingModule } from './poll-module-routing.module';
import { NewPollComponent } from './new-poll/new-poll.component';
import { PollHistoryComponent } from './poll-history/poll-history.component';
import { PollResultsComponent } from './poll-results/poll-results.component';
import { AttemptPollComponent } from './attempt-poll/attempt-poll.component';
import { PollLoginComponent } from './poll-login/poll-login.component';

@NgModule({
  declarations: [
    NewPollComponent,
    PollHistoryComponent,
    PollResultsComponent,
    AttemptPollComponent,
    PollLoginComponent
  ],
  imports: [
    CommonModule,
    FormsModule,
    ReactiveFormsModule,
    PollModuleRoutingModule,
    // SocketIoModule.forRoot(config)
  ]
})
export class PollModuleModule { }
