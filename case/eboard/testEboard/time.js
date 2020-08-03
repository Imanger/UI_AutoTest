/**
 * Created by Zhiying.Liu on 2019-10-31.
 */

function appendZero(obj) {
                            if(obj<10) return "0" +""+ obj;
                            else return obj;
                         }
var day = new Date();day.setTime(day.getTime());

if(day.getMonth()<12){
                var end_time = day.getFullYear()+"-" + appendZero(day.getMonth()+1) + "-" + appendZero(day.getDate())+ "  " + appendZero(day.getHours()) + ":" + appendZero(day.getMinutes());
                     }else{
                     var end_time = (day.getFullYear()+1)+"-01" + "-01" + "  " + appendZero(day.getHours()) + ":" + appendZero(day.getMinutes());
                     }
// //
// function appendZero(obj) {
//                         if(obj<10) return "0" +""+ obj;
//                         else return obj;
//                      }
//                 var day = new Date();day.setTime(day.getTime()+4*60*60*1000);
//                  var end_time = day.getFullYear()+"-" + appendZero(day.getMonth()+1) + "-" + appendZero(day.getDate())+ "  " + appendZero(day.getHours()) + ":" + appendZero(day.getMinutes());
//                  document.querySelector(".endTime--1jfcujQEBkSTgz9G0wLaTM").innerHTML=end_time
