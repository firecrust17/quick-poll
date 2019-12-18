import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PollHistoryComponent } from './poll-history.component';

describe('PollHistoryComponent', () => {
  let component: PollHistoryComponent;
  let fixture: ComponentFixture<PollHistoryComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PollHistoryComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PollHistoryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
