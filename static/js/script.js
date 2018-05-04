function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i += 1) {
      const cookie = jQuery.trim(cookies[i]);
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (`${name}=`)) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}


function renderTemplate(name, data) {
    let template = document.getElementById(name).innerHTML;

    for (let property in data) {
        if (data.hasOwnProperty(property)) {
            let search = new RegExp('{' + property + '}', 'g');
            template = template.replace(search, data[property]);
        }
    }
    return template;
}


$(document).ready(function () {
    render('http://127.0.0.1:8000/api/tasks/list')
});

function render(url_pattern) {

    main_html = $('.task-container');
    main_html.empty();

    $.getJSON(url_pattern, function (data) {
        for (let i in data) {
            if (data[i].is_complete) {
                data[i].is_complete_plural = 'Done'
            } else {
                data[i].is_complete_plural = 'Not done'
            }

            html = renderTemplate('template-task', {
                id: data[i].id,
                text: data[i].text,
                is_complete: data[i].is_complete,
                is_complete_plural: data[i].is_complete_plural
            });
            main_html.append(html);
        }
    });

}


$(document).on('click', '.task-state', function (event) {
    element = event.currentTarget;
    let task_id = element.id;
    let is_complete = element.dataset.complete;
    const csrfToken = getCookie('csrftoken');
    $.ajaxSetup({
        beforeSend(xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type)) {
                xhr.setRequestHeader('X-CSRFToken', csrfToken);
            }
        },
    });

    $.ajax({
        url: "http://127.0.0.1:8000/api/tasks/"+task_id+"/",
        type: "PUT", // or "get"
        success: function(data) {
            render('http://127.0.0.1:8000/api/tasks/list');
    }});

});



$(document).on('click', '.task-delete', function (event) {
    element = event.currentTarget;
    let task_id = element.id;

    const csrfToken = getCookie('csrftoken');
    $.ajaxSetup({
        beforeSend(xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type)) {
                xhr.setRequestHeader('X-CSRFToken', csrfToken);
            }
        },
    });

    $.ajax({
        url: 'http://127.0.0.1:8000/api/tasks/'+task_id+'/',
        type: 'DELETE',
        success: function(data) {
            element.parentElement.remove();
    }});

});

$( '#create-task-form' ).submit(function( event ) {
    event.preventDefault();

    let $form = $(this),
    text = $form.find( "input[name='text']" ).val();

    const csrfToken = getCookie('csrftoken');
    $.ajaxSetup({
        beforeSend(xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type)) {
                xhr.setRequestHeader('X-CSRFToken', csrfToken);
            }
        },
    });

    $.ajax({
        url: "http://127.0.0.1:8000/api/tasks/",
        type: "POST", // or "get"
        data: {
            text: text,
            is_complete: false
        },
        success: function(data) {
            render('http://127.0.0.1:8000/api/tasks/list');
    }});

});

