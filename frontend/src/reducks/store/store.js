
import { legacy_createStore as reduxCreateStore, combineReducers, applyMiddleware, compose } from 'redux';
import thunk from 'redux-thunk';

import { PostsReducer } from '../posts/reducers';
import { ItemsReducer } from '../items/reducers';
import { CartsReducers } from '../cart/reducers';

export default function createStore(history) {
    return reduxCreateStore(
        combineReducers({
            posts: PostsReducer,
            items: ItemsReducer,
            carts: CartsReducers,
        }),
        compose(
            applyMiddleware(thunk)
            // DEBUG MODE
            // window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()
        )
    );
}
