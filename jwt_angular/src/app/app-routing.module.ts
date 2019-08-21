import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';
import { LogoutComponent } from './logout/logout.component';
import { UserContentComponent } from './user-content/user-content.component';
import { AdminContentComponent } from './admin-content/admin-content.component';
import { AccessDeniedComponent } from './access-denied/access-denied.component';
import { AuthGuard } from './services/auth.guard';
import { AdminGuard } from './services/admin.guard';


const routes: Routes = [
  {
    path: '',
    component: HomeComponent,
    canActivate: [AuthGuard],
    canActivateChild: [AuthGuard],
    children: [
      {
        path: 'user-content',
        component: UserContentComponent
      },
      {
        path: 'admin-content',
        component: AdminContentComponent,
        canActivate: [AdminGuard]
      },
      {
        path: 'denied',
        component: AccessDeniedComponent
      }
    ]
  },
  {
    path: 'login',
    component: LoginComponent
  },
  {
    path: 'logout',
    component: LogoutComponent,
    canActivate: [AuthGuard]
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
