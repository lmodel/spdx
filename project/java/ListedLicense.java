package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.1 */
import java.util.List;
import lombok.*;

/**
  A license that is listed on the SPDX License List.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ListedLicense extends License {

  private String deprecatedVersion;
  private String listVersionAdded;

}