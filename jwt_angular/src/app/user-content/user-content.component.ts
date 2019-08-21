import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { UserObject } from '../models/user-object';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { environment } from 'src/environments/environment';


@Component({
  selector: 'app-user-content',
  templateUrl: './user-content.component.html',
  styleUrls: ['./user-content.component.css']
})
export class UserContentComponent implements OnInit {
  message = '';
  userForm = new FormGroup({
    example: new FormControl(null, Validators.required)
  });

  constructor(private http: HttpClient) { }

  ngOnInit() {
    this.http.get<UserObject>(environment.appServer + '/api/user-sample').subscribe(
      (userObj) => {
        this.userForm.get('example').setValue(userObj.example);
      },
      (error) => {
        this.message = 'Get failed: ' + error;
      }
    );
  }

  onSubmit() {
    this.http.post<UserObject>(environment.appServer + '/api/user-sample', {
      example: this.userForm.get('example').value
    }).subscribe(
      (userObj) => {
        this.userForm.get('example').setValue(userObj.example);
      },
      (error) => {
        console.log(error);
        this.message = 'Post failed: ' + error;
      }
    );
  }
}
