function get_dbs(searchBlock) {
    fetch('/dbs')
      .then(response => response.json())
      .then(data => {
        const searchType = document.createElement('select');
        searchType.className = 'search-company';
  
        // Create an option for each item in the data object
        Object.keys(data.data).forEach(key => {
          const option = document.createElement('option');
          option.value = key;
          option.textContent = data.data[key].name;
          searchType.appendChild(option);
        });
  
        // Add the select element to the DOM
        searchBlock.appendChild(searchType);
  
        const inputField = document.createElement('input');
        inputField.type = 'text';
        inputField.className = 'input-field';
        searchBlock.appendChild(inputField);
      });
  }

  
function set_search_block() {
    const searchBlock = document.createElement('div');
    searchBlock.className = 'search-block';
    get_dbs(searchBlock);

    searchesDiv.appendChild(searchBlock);

}