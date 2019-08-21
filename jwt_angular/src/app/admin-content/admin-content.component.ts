import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { AdminObject } from '../models/admin-object';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { environment } from 'src/environments/environment';


@Component({
  selector: 'app-admin-content',
  templateUrl: './admin-content.component.html',
  styleUrls: ['./admin-content.component.css']
})
export class AdminContentComponent implements OnInit {
  message = '';
  adminForm = new FormGroup({
    example: new FormControl(null, Validators.required)
  });

  constructor(private http: HttpClient) { }

  ngOnInit() {
    this.http.get<AdminObject>(environment.appServer + '/api/admin-sample').subscribe(
      (adminObj) => {
        this.adminForm.get('example').setValue(adminObj.example);
      },
      (error) => {
        this.message = 'Get failed: ' + error;
      }
    );
  }

  onSubmit() {
    this.http.post<AdminObject>(environment.appServer + '/api/admin-sample', {
      example: this.adminForm.get('example').value
    }).subscribe(
      (adminObj) => {
        this.adminForm.get('example').setValue(adminObj.example);
      },
      (error) => {
        this.message = 'Post failed: ' + error;
      }
    );
  }
}
