import React, {useState, useEffect} from 'react'
import './App.css';

function App() {
  // Initializing all the review state variables
  const [review, setReview] = useState([])
  const [comment, setComment] = useState("")
  const [rate, setRate] = useState("")

  //Fetching the movie data from flask
  useEffect(() => {

    fetch("/MovieData").then(
      res => res.json()
    ).then(
      data => {
        setReview(data)
      }
    )

  },[])

  // Delete a review based on id
 function deleteReview(e){  
    var id = e.target.id  
    fetch(`/MovieData/${id}`,{
      method: 'POST',
      body:JSON.stringify({
          id:id
      })
  }).then(response => response.json())
    
  alert("Review Deleted! When page is refreshed, it won't display in your profile.")
      
  }

  //Update a review based on id
  function updateReview(e){ 
    var id = e.target.className
    console.log(e.target.className)
    fetch(`/MovieData/${id}`, {
      method: "PUT",
      body: JSON.stringify({
          rate: rate,
          comment: comment
      }),
      headers: {
          "Content-type": "application/json; charset=UTF-8",
      },
  })
      .then((response) => response.json())

      alert("Review saved! When page is refreshed, it will display in your profile.")
  }
  // Return the movie data and display on the react server page
    return (
     <div>
<ul>
<h1>Your Reviews:</h1>
                {review.map((userReview, i) =>
                <div>
                 <b><p key={i}>Movie ID: {userReview.movieID}</p></b>
                 <input onChange={event => setRate(event.target.value)}size="4" key={i} defaultValue={userReview.rate}/>
                 <input onChange={event => setComment(event.target.value)} size="50"key={i} defaultValue={userReview.comment}/>
                 <button onClick={updateReview} className={userReview.id}>Update Review</button>
                 <button onClick={deleteReview} id={userReview.id}>delete</button>
                 </div>
                 
                 )}
            </ul>

      
     </div>

      
    )
}

export default App;
