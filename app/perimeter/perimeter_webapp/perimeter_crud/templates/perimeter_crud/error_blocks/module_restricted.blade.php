@extends('layouts.app')

@section('content')
	<div class="full-height d-flex align-content-center justify-content-center align-items-center w-100 row">
		<div class="col-12 flex-center position-ref ">
    	    <div class="code">Oops... </div>
				
			<div class="message" style="padding: 10px;">
        		<span class="fa fa-terminal"></span> You're not allowed to go there...
        	</div>
    			
    	</div>
    	<div class="explanation col-12 d-flex align-content-center justify-content-center align-items-center">
        	Your account hasn't been approved yet. Please contact your&nbsp;<a href="mailto:itsupport@ptcmw.com">system administrator.</a>
        </div>
        <div class="redirect my-3 col-12 d-flex align-content-center justify-content-center">
        	<button class="btn btn-outline-dark" onclick="history.back()"><span class="fa fa-arrow-left"></span> 
        		Return to where you were...
        	</button>
        </div>
    </div>
@endsection