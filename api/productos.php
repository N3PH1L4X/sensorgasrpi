<?php

    $conn = mysqli_connect('localhost', 'root', '19asd19asd', 'bddcesfam');

    //echo 'Informacion: ' . file_get_contents('php://input');
    switch($_SERVER['REQUEST_METHOD']){
        case 'POST':
            $_POST = json_decode(file_get_contents('php://input'), True);

            $nombre = $_POST['nombreProducto'];
            $fabrica = $_POST['fabricaProducto'];
            $descripcion = $_POST['descripcionProducto'];
            $cantidad = $_POST['cantidadProducto'];
            $gramaje = $_POST['gramajeProducto'];

            $insert = "INSERT INTO productos (nombreProducto,fabricaProducto,descripcionProducto,cantidadProducto,gramajeProducto)
                       VALUES ('$nombre','$fabrica','$descripcion','$cantidad','$gramaje')";
                    
            if (mysqli_query($conn,$insert)){
                echo "Registro guardado con exito";
            }else{
                echo "El registro no se pudo guardar". mysqli_error($conn);
            }
            mysqli_close($conn);
        break;

        case 'GET':
            
            $emparray = array();

            if (empty($_GET)) {
                $selectvacio = "SELECT * FROM productos";
                $respuesta = mysqli_query($conn, $selectvacio);
                while($row = mysqli_fetch_assoc($respuesta)){
                    $emparray[] = $row;
                }
                echo json_encode($emparray);
            }else{
                $id = $_GET['id'];
                $selectconalgo = "SELECT * FROM productos WHERE id = '$id'";
                $respuesta = mysqli_query($conn, $selectconalgo);
                while($row = mysqli_fetch_assoc($respuesta)){
                    $emparray[] = $row;
                }
                echo json_encode($emparray);
            }
            mysqli_close($conn);
        break;

        case 'PUT':
            //No hace nada, no es necesario para el caso
        break;

        case 'DELETE':
            $id = $_GET['id'];
            $borrar = "DELETE FROM productos WHERE id = '$id'";

            if (empty($_GET)) {
                //Si está vacio no hace nada
            }else{
                mysqli_query($conn,$borrar);
                echo "Producto $id borrado";
            }
            mysqli_close($conn);
        break;
    }
    
?>