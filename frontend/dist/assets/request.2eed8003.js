import{a as s}from"./axios.7aed06b8.js";const r=s.create({baseURL:"https://zxiaosi.deta.dev:8000/api/",timeout:2e4});r.interceptors.request.use(e=>e,e=>(console.log(e),Promise.reject()));r.interceptors.response.use(e=>{if(e.status===200)return e.data;Promise.reject()},e=>(console.log(e),Promise.reject()));export{r as s};
