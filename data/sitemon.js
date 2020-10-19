var sites = new Array(43);

sites[0] = "Victoria Avenue Spar_172.26.2.2_8080";
sites[1] = "Chitawira PCC_172.26.1.2_8080";
sites[2] = "Limbe Supersave_172.26.3.2_8080";
sites[3] = "Nandos Spar_172.26.4.2_8080";
sites[4] = "Blantyre Metro_172.26.5.2_8080";
sites[5] = "Namiwawa PCC_172.26.6.2_8080";
sites[6] = "City Center Spar_172.26.7.250_8080";
sites[7] = "Nico Center Spar_172.26.8.2_8080";
sites[8] = "Northgate Spar_172.26.10.2_8080";
sites[9] = "Mibawa PCC_172.26.11.2_8080";
sites[10] = "Kudya Spar_172.26.12.2_8080";
sites[11] = "Malangalanga_172.26.13.2_8080";
sites[12] = "Limbe Metro_172.26.14.2_8080";
sites[13] = "Zomba PCC_172.26.15.2_8080";
sites[14] = "Balaka PCC_172.26.18.2_8080";
sites[15] = "Liwonde PCC_172.26.19.2_8080";
sites[16] = "Kanengo Express_172.26.21.2_8080";
sites[17] = "Crossroads Express_172.26.22.2_8080";
sites[18] = "Nyambadwe Express_172.26.23.2_8080";
sites[19] = "Kabula Express_172.26.24.2_8080";
sites[20] = "Thyolo PCC_172.26.25.2_8080";
sites[21] = "Mwanza PCC_172.26.27.2_8080";
sites[22] = "Mangochi PCC_172.26.29.2_8080";
sites[23] = "Ntcheu PCC_172.26.30.2_8080";
sites[24] = "Mulanje PCC_172.26.31.2_8080";
sites[25] = "Dedza PCC_172.26.32.2_8080";
sites[26] = "Lilongwe Supersave_172.26.33.2_8080";
sites[27] = "Area 12_172.26.35.2_8080";
sites[28] = "Area 18_172.26.36.2_8080";
sites[29] = "Mchinji PCC_172.26.38.2_8080";
sites[30] = "Salima PCC_172.26.39.2_8080";
sites[31] = "Dwangwa PCC_172.26.41.2_8080";
sites[32] = "Mzimba PCC_172.26.44.2_8080";
sites[33] = "Nkhatabay PCC_172.26.45.2_8080";
sites[34] = "Uliwa PCC_172.26.47.2_8080";
sites[35] = "Karonga PCC_172.26.48.2_8080";
sites[36] = "Kasungu PCC_172.26.49.2_8080";
sites[37] = "Kasasa PCC_172.26.51.2_8080";
sites[38] = "Kameza PCC_172.26.53.2_8080";
sites[39] = "Fresh Foods_172.25.0.15_8080";
sites[40] = "Blantyre DC_172.25.0.11_8080";
sites[41] = "Mzuzu Supersave_172.25.2.52_8080";
sites[42] = "Mzuzu Metro_172.25.2.102_8080";

addSites();
initializeSearch();
initializeSelect();

function addSites() {
  document.getElementById("sites").innerHTML = "";

  var i = 0;

  for (; i < sites.length; i++) {
    var site = sites[i];
    site = site.split("_");

    addSite(site[0], site[1], site[2]);
  }
}

function initializeSearch() { 
  var search = document.getElementById("search_shop");
  search.addEventListener("keyup", function() {
    filterByValue();
  });
}

function filterByValue() {
  var search = document.getElementById("search_shop");
  var value = search.value.toLowerCase(); // Make it case neutral
  let i = 0;
  
  for (; i < sites.length; i++) {
    var site_params = sites[i].split("_");
    var site_name = site_params[0];
    var formattedSiteName = site_name.replace(/\ /g,'_');

    var site_entry = document.getElementsByClassName(formattedSiteName)[0];
          
    site_entry = site_entry.parentNode;

    if (site_name.toLowerCase().indexOf(value) > -1) {
      site_entry.style.display = "";
    } else {
      site_entry.style.display = "none";
    }
  }
}

function filterByConnectionStatus() {

  var connection_status = document.getElementById("filter_connection_status").value.toLowerCase();
  var site_wrappers = document.getElementsByClassName("site_wrapper");
  var i = 0;
  
  for (; i < site_wrappers.length; i++) {
    var site_wrapper = site_wrappers[i];
    var className = site_wrapper.className;
    if(className.indexOf("site-online") > -1) {
      if (connection_status.indexOf("online") > -1
          || connection_status.indexOf("all") > -1) {
        site_wrapper.style.display = "";
      } else {
        site_wrapper.style.display = "none";
      }
    } else if (className.indexOf("site-offline") > -1) {
      if (connection_status.indexOf("offline") > -1
          || connection_status.indexOf("all") > -1) {
        site_wrapper.style.display = "";
      } else {
        site_wrapper.style.display = "none";
      }
    } else if (className.indexOf("site-pending") > -1) {
      if (connection_status.indexOf("all") > -1
        || connection_status.indexOf("pending") > -1) {
        site_wrapper.style.display = "";
      } else {
        site_wrapper.style.display =  "none"
      }
    }
  }
}

function addSite(sitename, siteAddress, port) {
  var dashboard = document.getElementById("sites");
  var entry = createSiteEntry(sitename, siteAddress, port);
  dashboard.appendChild(entry);
  checkConnectivityStatus(sitename, siteAddress, port);
}

function createSiteEntry(sitename, siteAddress, port) {
  var paragraph = document.createElement("p");
  paragraph.className = "site_wrapper site-pending";

  var link = document.createElement("a");
  link.className = sitename.replace(/\ /g,'_') + " site_link";
  link.href = "http://" + siteAddress + ":" + port + "/backoffice";

  var sitename_span = document.createElement("span");
  sitename_span.className = "site_name";
  sitename_span.innerHTML = sitename;
  
  var connectivity_status = document.createElement("span");
  connectivity_status.className = "connectivity_status";
  
  var indicator = document.createElement("span");
  indicator.className = "indicator";
  indicator.innerHTML = '<div class="lds-facebook"><div></div><div></div><div></div></div>';
        
  connectivity_status.innerHTML = "Attempting to connect...";

  connectivity_status.insertBefore(indicator, connectivity_status.childNodes[0]);

  link.appendChild(sitename_span);
  link.appendChild(connectivity_status);

  paragraph.appendChild(link);

  return paragraph;
}

function checkConnectivityStatus(sitename, siteAddress, port) {
  var request = "/perimeter/php/sitemon.php?checktype=status&sitename=" + sitename + "&site_ip=" + siteAddress + "&port=" + port;
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      updateSiteStatus(sitename, siteAddress, this.responseText);
    }
  };
  xhttp.open("GET", request, true);
  xhttp.send();
}
      
function updateSiteStatus(sitename, siteAddress, responseText) {
  var formattedClassName = sitename.replace(/\ /g,'_');
  var site_entry = document.getElementsByClassName(formattedClassName)[0];
  
  site_entry = site_entry.parentNode;
  site_entry.classList.toggle("site-pending");

  if (responseText.toLowerCase().indexOf("online") > -1) {
    site_entry.classList.toggle("site-online");
  } else if (responseText.toLowerCase().indexOf("offline") > -1) {
    site_entry.classList.toggle("site-offline");
  }

  var connectivity_status = site_entry.getElementsByClassName("connectivity_status")[0];
  var indicator = connectivity_status.getElementsByClassName("indicator")[0];
  indicator.innerHTML = "";
  connectivity_status.innerHTML = "<pre>" + responseText + "</pre>";
}


function initializeSelect() {
  var x, i, j, selElmnt, a, b, c;
  /* Look for any elements with the class "custom-select": */
  x = document.getElementsByClassName("custom-select");
  for (i = 0; i < x.length; i++) {
    selElmnt = x[i].getElementsByTagName("select")[0];
    /* For each element, create a new DIV that will act as the selected item: */
    a = document.createElement("DIV");
    a.setAttribute("class", "select-selected");
    a.innerHTML = selElmnt.options[selElmnt.selectedIndex].innerHTML;
    x[i].appendChild(a);
    /* For each element, create a new DIV that will contain the option list: */
    b = document.createElement("DIV");
    b.setAttribute("class", "select-items select-hide");

    for (j = 1; j < selElmnt.length; j++) {
      /* For each option in the original select element,
      create a new DIV that will act as an option item: */
      c = document.createElement("DIV");
      c.innerHTML = selElmnt.options[j].innerHTML;
      c.addEventListener("click", function(e) {
        /* When an item is clicked, update the original select box,
        and the selected item: */
          var y, i, k, s, h;
          s = this.parentNode.parentNode.getElementsByTagName("select")[0];
          h = this.parentNode.previousSibling;
          
          for (i = 0; i < s.length; i++) {
            if (s.options[i].innerHTML == this.innerHTML) {
              s.selectedIndex = i;
              h.innerHTML = this.innerHTML;
              y = this.parentNode.getElementsByClassName("same-as-selected");
              for (k = 0; k < y.length; k++) {
                y[k].removeAttribute("class");
              }
              this.setAttribute("class", "same-as-selected");
              break;
            }
          }
          h.click();

          filterByConnectionStatus();
      });
      b.appendChild(c);
    }
    
    x[i].appendChild(b);
    
    a.addEventListener("click", function(e) {
      /* When the select box is clicked, close any other select boxes,
      and open/close the current select box: */
      e.stopPropagation();
      closeAllSelect(this);
      this.nextSibling.classList.toggle("select-hide");
      this.classList.toggle("select-arrow-active");
    });
  }

  /* If the user clicks anywhere outside the select box,
  then close all select boxes: */
  document.addEventListener("click", closeAllSelect);
}

function closeAllSelect(elmnt) {
  /* A function that will close all select boxes in the document,
  except the current select box: */
  var x, y, i, arrNo = [];
  x = document.getElementsByClassName("select-items");
  y = document.getElementsByClassName("select-selected");
  for (i = 0; i < y.length; i++) {
    if (elmnt == y[i]) {
      arrNo.push(i)
    } else {
      y[i].classList.remove("select-arrow-active");
    }
  }
  for (i = 0; i < x.length; i++) {
    if (arrNo.indexOf(i)) {
      x[i].classList.add("select-hide");
    }
  }
}