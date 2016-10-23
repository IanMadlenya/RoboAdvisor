import React from 'react';

import ApiContainer from '../../../common/components/ApiContainer';
import Pi from '../../../common/components/Pi';

const ImpactingAssets = ({ impactingAssets }) => {

  let element,
    data = impactingAssets.data;

  if (data) {

    element = <ul className="list-table">
      { data.map((asset, index) => {
          if (index < 5) {
            return <li key={index} className="list__item flex-row">
              <div className="flex-row__item">
                <strong>
                  <Pi {...{value: asset.prediction}} />
                </strong>
              </div>
              <div className="flex-row__item">
                <strong>{asset.asset}</strong>
              </div>
            </li>
          }
        }
      )}
    </ul>
  }

  return <ApiContainer {...{
    isFetching: impactingAssets.isFetching,
    isFailed: impactingAssets.isFailed,
    element: element
  }}></ApiContainer>
};

export default ImpactingAssets;