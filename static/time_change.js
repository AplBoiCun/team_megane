function start_time_change(time){
  moment.locale('ja', {weekdays: ["日","月","火","水","木","金","土"]});
  return moment(time).format('M月D日(dddd曜)HH:mm');
}
function end_time_change(time){
  return moment(time).format('HH:mm');
}
for(var i=0;i<50;i++){
var start_time = document.getElementById('start_time_change_'+String(i));
var end_time = document.getElementById('end_time_change_'+String(i));
start_time.innerHTML = "日時: "+start_time_change(start_time.textContent);
end_time.innerHTML = "~"+end_time_change(end_time.textContent);
}
