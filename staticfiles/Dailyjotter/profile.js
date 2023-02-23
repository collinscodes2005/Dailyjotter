const editLabel = document.querySelector('.edit-label');
    const inputFile = document.querySelector('#id_image');

    editLabel.addEventListener('click', () => {
        inputFile.click();
    });

    inputFile.addEventListener('change', () => {
        editLabel.classList.add('selected');
    });
