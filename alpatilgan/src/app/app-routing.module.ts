import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { FootballComponent } from './football/football.component';

const routes: Routes = [
  {path:'football', component:FootballComponent},
//  {path:'about'....}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
