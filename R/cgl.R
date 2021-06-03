# AUTO GENERATED FILE - DO NOT EDIT

cgl <- function(id=NULL, label=NULL, value_rows=NULL, value_cols=NULL, network=NULL, divId=NULL) {
    
    props <- list(id=id, label=label, value_rows=value_rows, value_cols=value_cols, network=network, divId=divId)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Cgl',
        namespace = 'stlcgl',
        propNames = c('id', 'label', 'value_rows', 'value_cols', 'network', 'divId'),
        package = 'stlcgl'
        )

    structure(component, class = c('dash_component', 'list'))
}
