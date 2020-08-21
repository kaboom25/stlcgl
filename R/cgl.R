# AUTO GENERATED FILE - DO NOT EDIT

cgl <- function(id=NULL, label=NULL, value=NULL, network=NULL) {
    
    props <- list(id=id, label=label, value=value, network=network)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Cgl',
        namespace = 'stlcgl',
        propNames = c('id', 'label', 'value', 'network'),
        package = 'stlcgl'
        )

    structure(component, class = c('dash_component', 'list'))
}
