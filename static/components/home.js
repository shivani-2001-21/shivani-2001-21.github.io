
export default{
    template:`
    <div> 
        
        <center>
        <br>
        <h3> Hello Admin </h3>
        <p><button type="button" class="btn btn-dark" ><router-link to="/adminhome"> Admin Home </router-link></button></p>

            <button type="button" class="btn btn-dark" ><router-link to="/addtheatre"> Add Theatre </router-link></button>
            <button type="button" class="btn btn-dark" ><router-link to="/addshow"> Add Show </router-link></button>
            <button type="button" class="btn btn-dark" ><router-link to="/addscreening"> Add Screening </router-link></button>
            <br>
            <br>
        <br>
        <div class="alert alert-warning" role="alert" v-if="not_exported"> Export file first </div>
       <h3> All Shows </h3>
       <div class="row">
                    <div class="card my-3 mx-4 col-4" style="width: 20rem;" v-for="show in show" :key="id">
                                <div class="card-body">
                                    <h3 class="card-title">{{show['Name']}}</h3>
                                    <h6 class="card-text">Tag : {{show['Tag']}} </h6>
                                    <h6 class="card-text">Rating : {{show['Rating'] }}</h6>
                                    <h6 class="card-text">Price : {{show['Ticket_Price'] }}</h6>
                                    <h6 class="card-text">ID : {{show['id'] }}</h6>
                                    <a class="btn" @click="edit(show['id'])" >Edit Show </a> 
                                    <a class="btn" @click="dlt_show(show['id'])"> Delete Show </a>
                                    <a class="btn" @click="export_data('s',show['id'])"> Export </a>
                                    <a class="btn" @click="download_data('s',show['id'])"> Download </a>

                                </div>
                    </div>
                </div>


       <h3> All Theatres </h3>
       <div class="row">
                    <div class="card my-3 mx-4 col-4" style="width: 20rem;" v-for="theatre in theatre" :key="id">
                                <div class="card-body">
                                    <h3 class="card-title">{{theatre['Name']}}</h3>
                                    <h6 class="card-text">Place : {{theatre['Place']}} </h6>
                                    <h6 class="card-text">Capacity : {{theatre['Capacity'] }}</h6>
                                    <h6 class="card-text">ID : {{theatre['id'] }}</h6>
                                    <a class="btn" @click="edit_theatre(theatre['id'])" >Edit Theatre </a> 
                                    <a class="btn" @click="dlt_theatre(theatre['id'])"> Delete Theatre </a>
                                    <a class="btn" @click="export_data('t',theatre['id'])"> Export </a>
                                    <a class="btn" @click="download_data('t',theatre['id'])"> Download </a>

                                </div>
                    </div>
                </div>

        </center>
    </div>

    `}
