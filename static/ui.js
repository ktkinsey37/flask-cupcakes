$getAllCupcakes = $("#get-all-cupcakes")

$getAllCupcakes.on('click', async function(evt){
    evt.preventDefault()
    await updateCupcakeList()
    }
)

async function updateCupcakeList(){
    $("#cupcake-list").empty()
    const response = await axios.get('http://127.0.0.1:5000/api/cupcakes')
    for (let cupcake of response.data.cupcakes){
        let li = document.createElement('li')
        li.innerHTML = cupcake.flavor
        li.setAttribute('data-id', `${cupcake.id}`)
        let btn = document.createElement('button')
        btn.innerHTML = "Delete Cupcake"
        li.append(btn)
        btn.addEventListener("click", function(evt){
            evt.preventDefault()
            deleteCupcake($(this))
        })
        $("#cupcake-list").append(li)
    }

}

$("#add-cupcake").on('click', async function(evt){
    evt.preventDefault()
    response = await addCupcake()
    console.log(response)
})

async function addCupcake(){
    const response = await axios.post('http://127.0.0.1:5000/api/cupcakes',
    {flavor: `${$("#flavor").val()}`,
    size: `${$("#size").val()}`,
    rating: `${$("#rating").val()}`,
    image: `${$("#image").val()}`,
})
    $(".add-cupcake-input").val('')
    updateCupcakeList()
    return response
}

async function deleteCupcake(cupcake){
    const x = cupcake.closest('li')
    const id = x.data("id")
    const response = await axios.delete(`http://127.0.0.1:5000/api/cupcakes/${id}`)
    console.log(response)
    updateCupcakeList()
}