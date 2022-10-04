<?php

    $conn = mysqli_connect('localhost', 'root', '19asd19asd', 'rpi_sensor');

    //echo 'Informacion: ' . file_get_contents('php://input');
    switch($_SERVER['REQUEST_METHOD']){
        case 'POST':
            $_POST = json_decode(file_get_contents('php://input'), True);

            $temperatura = $_POST['temperatura'];
            $humedad = $_POST['humedad'];

            $insert = "INSERT INTO lectura (temperatura,humedad)
                       VALUES ('$temperatura','$humedad')";
                    
            if (mysqli_query($conn,$insert)){
                echo "Registro guardado con exito";
            }else{
                echo "El registro no se pudo guardar". mysqli_error($conn);
            }
            mysqli_close($conn);
        break;

        case 'GET':
            header('Content-Type: application/json');
            $emparray = array();

            $select = "SELECT temperatura,humedad FROM lectura ORDER BY id DESC LIMIT 0,1";
            $respuesta = mysqli_query($conn, $select);
            
            while($row = mysqli_fetch_assoc($respuesta)){
                $emparray[] = $row;
            }
            echo json_encode($emparray);
            
            mysqli_close($conn);

        break;

    }
    
?>
