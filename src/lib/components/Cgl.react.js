import React, {Component} from 'react';
import PropTypes from 'prop-types';
import CGM from '../clustergrammerGL/clustergrammer-gl.node'

/**
 * ExampleComponent is an example component.
 * It takes a property, `label`, and
 * displays it.
 * It renders an input with the property `value`
 * which is editable by the user.
 */
var cgm = null;
export default class Cgl extends Component {
    constructor(props) {
        super(props);
        this.state = { value: [] }
    }

    componentDidMount() {
        //callbacks
        //called when user clicks on trapezoids.
        const my_dendro_click_callback = function () {
            if (cgm != null) {
                //emit event that says dendro was clicked
                let selectionEvent = new CustomEvent('cluster_selection', { detail: cgm.params.dendro.selected_clust_names })
                document.getElementById(cgm.args.reactComp.props.id).dispatchEvent(selectionEvent)
            }
        };

        //listener for dendro_click event
        document.getElementById(this.props.id).addEventListener('cluster_selection',e =>
            {
                // this.setState({ value: e.detail })
                this.props.setProps({ value: e.detail})
                console.log('selected: ' + e.detail)
            }
        )



        const inst_container = document.getElementById(this.props.id);
        const inst_height = 900;
        const inst_width = 900;
        const network = JSON.parse(this.props.network)
        // hardwire manual category
        // network.manual_category = {}
        // network.manual_category.col = 'Cell Type'
        // network.manual_category.col_cats = [
        //     {
        //         'name':'Cat',
        //         'color':'red'
        //     },
        //     {
        //         'name': 'Dog',
        //         'color': 'yellow'
        //     },
        //     {
        //         'name': 'Shark',
        //         'color': 'black'
        //     },
        //     {
        //         'name': 'Snake',
        //         'color': 'blue'
        //     },
        //     {
        //         'name': 'Lizard',
        //         'color': 'green'
        //     }
        // ]

        // set matrix colors
        network.matrix_colors = {}
        network.matrix_colors.pos = 'red'
        network.matrix_colors.neg = 'blue'
        let args = {}
        args.network = network;
        args.container=inst_container;
        args.viz_width=inst_width;
        args.viz_height=inst_height;
        args.reactComp=this;
        args.dendro_click_callback = my_dendro_click_callback

        cgm = CGM(args);

    }

    render() {

        return (
            <div>
                <div id={this.props.id}>
                </div>
            </div>
        );
    }
}

Cgl.defaultProps = {};

Cgl.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    label: PropTypes.string,

    value: PropTypes.array,

    /**
     * added by Phillip
     * stringified clustergrammer-gl network object
     */
    network: PropTypes.string.isRequired,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};
