// console.log(" Working ")

// mydatas()


// // POST METHOD
// function addintodb(){
//     var myHeaders = new Headers();
//     myHeaders.append("Content-Type", "application/json");

//     var raw = JSON.stringify({
//     "product_code": document.getElementById('p_code').value,
//     "product_name": document.getElementById('p_name').value,
//     "product_details": document.getElementById('p_details').value,
//     "product_price": document.getElementById('p_price').value,
//     "product_purchase_date": document.getElementById('p_purchase_d').value,
//     "product_expired_date": document.getElementById('p_expired_d').value
//     });

//     var requestOptions = {
//     method: 'POST',
//     headers: myHeaders,
//     body: raw,
//     redirect: 'follow'
//         };

//     fetch("http://127.0.0.1:5000/api_post", requestOptions)
//         .then(response => response.text())
//         .then(result => console.log("Data Add Successfully"))
//         .catch(error => console.log('error', error));  
        
//         location.reload();
//         }
    


// function mydatas(){
//     var requestOptions = {
//         method: 'GET',
//         redirect: 'follow'
//       };
      
//       fetch("http://127.0.0.1:5000/api_get", requestOptions)
//         .then(response => response.json())
//         .then(result => {
//             console.log("All Products") 
//             for (var p in result.Paylod ){
//                 // var myid =result.Paylod[p]['_id']
//                 var product_code =result.Paylod[p]['product_code']
//                 var product_name =result.Paylod[p]['product_name']
//                 var product_price =result.Paylod[p]['product_price']
//                 var mytabledata =`
//                 <tr>
//                 <td>`+product_code +`</td>
//                 <td>`+product_name+`</td>
//                 <td>`+product_price +`</td>
//                 <td> 
//                 <button type="button" class="btn btn-danger" onclick=deleteme(`+product_code+`)>Delete</button>
//                 <a href="/updatepage/`+product_code+`"><button type="button" class="btn btn-success" onclick=updateme(`+product_code+`) >Update</button></a>                                                                   
//                 </td>
//                 </tr>`

//                 document.getElementById('mytable').innerHTML += mytabledata

//                 }})
//         .catch(error => console.log('error', error))
// }


// function deleteme(id){
//     console.log(id)
//     var requestOptions = {
//         method: 'DELETE',
//         redirect: 'follow'
//       };
      
//       fetch("http://127.0.0.1:5000//api_delete/"+ id, requestOptions)
//         .then(response => response.text())
//         .then(result => console.log("delete item " ))
//         .catch(error => console.log('error', error));
//     }
    


// function updateme(id){
//     console.log("update ----")

//     var requestOptions = {
//         method: 'PATCH',
//         redirect: 'follow'
//       };
      
//     fetch("http://127.0.0.1:5000/api_update/"+id, requestOptions)

//     update_page_opne(id)
// }

// function update_page_opne(id){
//     var requestOptions = {
//         method: 'PATCH',
//         redirect: 'follow'
//       };
//     fetch("http://127.0.0.1:5000/api_update/"+id, requestOptions)
// }