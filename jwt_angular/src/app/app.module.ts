import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { ReactiveFormsModule } from '@angular/forms';

import { AuthInterceptor } from './services/auth.interceptor';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { LogoutComponent } from './logout/logout.component';
import { HomeComponent } from './home/home.component';
import { UserContentComponent } from './user-content/user-content.component';
import { AdminContentComponent } from './admin-content/admin-content.component';
import { AccessDeniedComponent } from './access-denied/access-denied.component';


@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    LogoutComponent,
    HomeComponent,
    UserContentComponent,
    AdminContentComponent,
    AccessDeniedComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    ReactiveFormsModule,
    AppRoutingModule
  ],
  providers: [
    { provide: HTTP_INTERCEPTORS, useClass: AuthInterceptor, multi: true }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
