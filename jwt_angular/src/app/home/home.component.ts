import { Component, OnInit } from '@angular/core';
import { AuthService } from '../services/auth.service';


@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  authenticated: boolean;
  isAdmin: boolean;
  username: string;

  constructor(private auth: AuthService) { }

  ngOnInit() {
    this.auth.subscribe(
      (authenticated) => {
        this.authenticated = authenticated;
        if (authenticated) {
          this.username = this.auth.getUsername();
          this.isAdmin = this.auth.isAdmin();
        } else {
          this.username = undefined;
          this.isAdmin = false;
        }
      }
    );
  }
}
