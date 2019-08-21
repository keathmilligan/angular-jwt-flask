import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from '../services/auth.service';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  message = '';
  loginForm = new FormGroup({
    username: new FormControl('', Validators.required),
    password: new FormControl('', Validators.required)
  });

  constructor(private auth: AuthService,
              private router: Router) { }

  ngOnInit() {
  }

  onSubmit() {
    const username = this.loginForm.get('username').value;
    const password = this.loginForm.get('password').value;
    console.log(`logging in: ${username}`);
    this.auth.authenticate(username, password).subscribe(
      () => {
        this.router.navigate(['/']);
      },
      (error) => {
        this.message = error;
      }
    );
  }
}
