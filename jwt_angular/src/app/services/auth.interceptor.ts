import { Injectable } from '@angular/core';
import { HttpInterceptor, HttpEvent, HttpHandler, HttpRequest } from '@angular/common/http';
import { Router } from '@angular/router';
import { AuthService } from './auth.service';
import { Observable, throwError } from 'rxjs';
import { mergeMap, catchError } from 'rxjs/operators';


@Injectable()
export class AuthInterceptor implements HttpInterceptor {

  constructor(private auth: AuthService,
              private router: Router) { }

  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    if (!/.*\/api\/auth\/.*/.test(req.url)) {
      return this.auth.getAccessToken().pipe(
        mergeMap((accessToken: string) => {
          const reqAuth = req.clone({ setHeaders: { Authorization: `Bearer ${accessToken}` } });
          return next.handle(reqAuth);
        }),
        catchError((err) => {
          console.error(err);
          this.router.navigate(['/login']);
          return throwError(err);
        })
      );
    } else {
      return next.handle(req);
    }
  }
}
