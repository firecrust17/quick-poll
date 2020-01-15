import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PollLoginComponent } from './poll-login.component';

describe('PollLoginComponent', () => {
  let component: PollLoginComponent;
  let fixture: ComponentFixture<PollLoginComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PollLoginComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PollLoginComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
