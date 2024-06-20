// JavaScript to fetch data and update the DOM
document.addEventListener('DOMContentLoaded', function() {
    console.log("Hello");
    const addBtn = document.querySelector('.btn');

    // Setting the URL we want to navigate to
    const createProductUrl = 'http://127.0.0.1:8000/homeapi/create/';

    // Adding click event listener
    addBtn.addEventListener('click', function(event) {
        // Preventing default action of the anchor tag
        event.preventDefault();
        // Navigating to the URL
        window.location.href = createProductUrl;
    });
    
    fetch('http://127.0.0.1:8000/homeapi/list/')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            const blogListContainer = document.getElementsByClassName('blogs')[0];
            data.forEach(blog => {
                const blogItem = document.createElement('div');
                blogItem.classList.add('blog__card');
                blogItem.innerHTML = `
                    <ul>
                        <li>
                            <h1>${blog.author.username}</h1>
                            <h2>${truncate(blog.title, 20)}</h2>
                            <p>${truncate(blog.content, 70)}</p>
                            <img src="${blog.image.url}" alt="${truncate(blog.content, 20)}">
                            <h3>${blog.price} AZN</h3>
                            <h5>${blog.created_date}</h5>
                            <a href="/homeapi/update/${blog.id}"><i class="fa-solid fa-marker"></i></a>
                            <a href="/homeapi/delete/${blog.id}"><i class="fa-solid fa-trash"></i></a>
                            <a href="/homeapi/detail/${blog.id}"><i class="fa-solid fa-circle-info"></i></a>
                        </li>
                        <br><br>
                        <hr>
                    </ul>
                `;
                blogListContainer.appendChild(blogItem);
            });
        })
        .catch(error => {
            console.error('There has been a problem with your fetch operation:', error);
        });
});

// Function to truncate text
function truncate(text, length) {
    return text.length > length ? text.substring(0, length) + '...' : text;
}
