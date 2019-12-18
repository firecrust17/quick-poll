import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AttemptPollComponent } from './attempt-poll.component';

describe('AttemptPollComponent', () => {
  let component: AttemptPollComponent;
  let fixture: ComponentFixture<AttemptPollComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AttemptPollComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AttemptPollComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
