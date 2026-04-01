package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.1 */
import java.util.List;
import lombok.*;

/**
  A type of extension consisting of a list of name value pairs.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CdxPropertiesExtension extends Extension {

  private List<CdxPropertyEntry> cdxProperty;

}