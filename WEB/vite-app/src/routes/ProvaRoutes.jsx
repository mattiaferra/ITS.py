import React, { useState } from 'react';
import Home from "./Home";
import ErrorPage from './ErrorPage';
import About from "./About";
import Profiles from "./Profiles";
import SingleProfile from "./SingleProfile";
import MyProfile from "./MyProfile";
import { BrowserRouter, Routes, Route, Link, useRoutes } from "react-router-dom"
import { routes } from './routes';

const AppRoutes = () => {
    const elements = useRoutes(routes)
    return elements
}

const ProvaRoutes = () => {
    
  return (
    <div>
        <BrowserRouter>
            <nav className = 'navbar'>
                <Link to = "/">Home</Link>
                <Link to = "/about">About</Link>
                <Link to = "/Profiles">Profiles</Link>
            </nav>
            <hr></hr>
            <AppRoutes></AppRoutes>
            {/*<Routes>
                <Route path = "/" element = {<Home></Home>}></Route>
                <Route path = "/about" element = {<About></About>}></Route>
                <Route path = "/profiles" element = {<Profiles></Profiles>}>
                    <Route path = "/profiles/:id" element = {<SingleProfile></SingleProfile>}></Route>
                    <Route path = "/profiles/me" element = {<MyProfile></MyProfile>}></Route>
                </Route>
                <Route path = "*" element = {<ErrorPage></ErrorPage>}></Route>
            </Routes>*/}
        </BrowserRouter>
        <hr></hr>
    </div>
  );
};

export default ProvaRoutes;